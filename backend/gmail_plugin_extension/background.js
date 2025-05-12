let ipv4s = ["192.168.56.1", "192.168.1.74"]
let lastChecked = Date.now();

chrome.runtime.onInstalled.addListener(() => {
    console.log("Extension installed");
});

chrome.runtime.onMessage.addListener((msg) => {
    if (msg.startPolling) {
        chrome.alarms.create("pollGmail", { periodInMinutes: 0.1 });
        console.log("Polling started");
    }
});

chrome.alarms.onAlarm.addListener((alarm) => {
    if (alarm.name === "pollGmail") {
        chrome.storage.local.get("gmailToken", ({ gmailToken }) => {
            if (gmailToken) {
                checkForNewEmails(gmailToken);
            }
        });
    }
});

async function checkForNewEmails(token) {
    const query = `after:${Math.floor(lastChecked / 1000)}`;
    lastChecked = Date.now();

    try {
        const res = await fetch(
            `https://www.googleapis.com/gmail/v1/users/me/messages?q=${encodeURIComponent(query)}`,
            {
                method: "GET",
                headers: { Authorization: `Bearer ${token}` },
                Accept: "application/json"
            }
        );
        const data = await res.json();
        if (data.error) {
            if (data.error.code === 401) {
                console.log("Token expired. Reauthorizing...");
                chrome.storage.local.get("gmailToken", ({ gmailToken }) => {
                    console.log(gmailToken)
                    if (gmailToken) {
                        fetch("https://www.googleapis.com/oauth2/v3/tokeninfo?access_token=" + token)
                            .then(res => res.json())
                            .then(data => console.log("Token scopes:", data.scope));
                    }
                });
                chrome.storage.local.remove("gmailToken");
                chrome.identity.getAuthToken({ interactive: true }, (newToken) => {
                    if (chrome.runtime.lastError) {
                        console.error("Auth error:", chrome.runtime.lastError.message);
                    } else {
                        chrome.storage.local.set({ gmailToken: newToken }, () => {
                            checkForNewEmails(newToken);
                        });
                    }
                });
            }
            else {
                console.error("Error fetching emails:", data.error);
            }
            return;
        }
        if (data.messages && data.messages.length > 0) {
            console.log("Response data:", data);
            for (const msg of data.messages) {
                const msgRes = await fetch(
                    `https://www.googleapis.com/gmail/v1/users/me/messages/${msg.id}?format=full`,
                    {
                        method: "GET",
                        headers: { Authorization: `Bearer ${token}` }
                    }
                );
                const msgData = await msgRes.json();
                for (const idx in ipv4s) {
                    let ipv4 = ipv4s[idx];
                    try {
                        await fetch("http://" + ipv4 + ":5000/new-mail", {
                            method: "POST",
                            headers: { "Content-Type": "application/json" },
                            body: JSON.stringify(msgData)
                        });
                        console.log("data sent to " + ipv4);
                    }
                    catch (error) {
                        if (error instanceof TypeError) 
                            console.log(ipv4+" is not running");
                        else 
                            console.error("Error sending data to " + ipv4, error);
                    }
                }
            }
        }
    } catch (error) {
        console.error("Error fetching emails:", error);
    }
}
