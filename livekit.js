async function fetchSessionCredentials() {
    const response = await fetch('https://gdkau5zbrvyzeagmqrhgtytd4a0qnkwo.lambda-url.us-east-2.on.aws/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
    });

    const result = await response.json();
    
    if (!result.data || !result.data.session_token) {
        throw new Error("Session credentials missing from server response");
    }

    return {
        token: result.data.session_token,
        serverUrl: "wss://api.liveavatar.com/v1/ws" 
    };
}

// This function is what your website calls to start the avatar
async function startAvatarSession() {
    try {
        const credentials = await fetchSessionCredentials();
        console.log("Session obtained:", credentials.token);
        // LiveKit connection code goes here
    } catch (error) {
        console.error("Popup Triggered By:", error);
        alert("Credential Error: " + error.message);
    }
}
