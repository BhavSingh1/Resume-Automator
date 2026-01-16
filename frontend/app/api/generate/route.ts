import { NextResponse } from "next/server"

export async function POST(req: Request) {
  const body = await req.json()

  // Proxy to backend
  const res = await fetch("http://localhost:8000/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  })

  const data = await res.json()
  return NextResponse.json(data)
}
