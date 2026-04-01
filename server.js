// This acts as a mini-server to fetch your token securely
export async function getSessionToken() {
  const response = await fetch("https://api.liveavatar.com/v1/sessions/token", {
    method: "POST",
    headers: {
      "X-API-KEY": process.env.LIVEAVATAR_API_KEY, // We will set this in the Amplify Console
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      "mode": "FULL",
       "avatar_id": "513fd1b7-7ef9-466d-9af2-344e51eeb833",
       "avatar_persona": {
         "voice_id": "c2527536-6d1f-4412-a643-53a3497dada9",
         "context_id": "83b3a3f8-2f3f-4b97-8837-66fc1688b268"
      }
    })
  });
  return await response.json();
}


