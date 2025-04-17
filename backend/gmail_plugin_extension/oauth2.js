document.getElementById("authorize").addEventListener("click", () => {
    document.getElementById("status").textContent = "Authorizing...";

    chrome.identity.getAuthToken({ interactive: true }, (token) => {
      if (chrome.runtime.lastError) {
        console.error("Auth error:", chrome.runtime.lastError.message);
        document.getElementById("status").textContent =
          "Authorization canceled or failed.";
      } else {
        chrome.storage.local.set({ gmailToken: token }, () => {
          document.getElementById("status").textContent = "Connected!";
          chrome.runtime.sendMessage({ startPolling: true });
        });
      }
    });
  });
  