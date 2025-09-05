import { useEffect, useState } from 'react'

export default function App() {
  const [health, setHealth] = useState<string>('loading...')
  useEffect(() => {
    fetch('http://localhost:8000/health')
      .then(r => r.json())
      .then(j => setHealth(j.status))
      .catch(() => setHealth('error'))
  }, [])

  return (
    <div style={{ fontFamily: 'system-ui', padding: 24 }}>
      <h1>Capstone Starter</h1>
      <p>Backend health: <strong>{health}</strong></p>
      <p>Try creating a user via <code>POST /api/v1/users</code> and listing them via <code>GET /api/v1/users</code>.</p>
      <p>Open API docs: <a href="http://localhost:8000/docs" target="_blank">http://localhost:8000/docs</a></p>
    </div>
  )
}
