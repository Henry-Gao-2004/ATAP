document.getElementById('authorize').addEventListener('click', function () {
    document.getElementById('status').textContent = 'Authorizing...';
  
    chrome.identity.getAuthToken({ interactive: true }, function (token) {
      if (chrome.runtime.lastError) {
        document.getElementById('status').textContent = 'Authorization failed: ' + chrome.runtime.lastError.message;
      } else {
        document.getElementById('status').textContent = 'Authorized successfully!';
        console.log('OAuth Token:', token);
        
        // Optional: Store token in chrome.storage for background script
        chrome.storage.local.set({ gmailToken: token });
      }
    });
  });
  