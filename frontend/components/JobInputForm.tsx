"use client"

import { useState } from "react"
import ATSScoreCard from "./ATSScoreCard"
import ResumePreview from "./ResumePreview"
import BulletList from "./BulletList"

export default function JobInputForm() {
  const [jobDescription, setJobDescription] = useState("")
  const [result, setResult] = useState<any>(null)
  const [loading, setLoading] = useState(false)

  async function handleSubmit() {
    setLoading(true)

    const res = await fetch("/api/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        profile: {},
        job_description: jobDescription,
      }),
    })

    const data = await res.json()
    setResult(data)
    setLoading(false)
  }

  return (
    <>
      <textarea
        className="w-full h-40 p-3 border rounded mb-4"
        placeholder="Paste job description..."
        value={jobDescription}
        onChange={(e) => setJobDescription(e.target.value)}
      />

      <button
        onClick={handleSubmit}
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        Generate Resume
      </button>

      {loading && <p className="mt-4">⏳ Processing...</p>}

      {result && (
        <>
          <ATSScoreCard score={result.ats_score} />
          <BulletList bullets={result.bullets} />
          <ResumePreview pdfUrl={result.pdf_url} />
        </>
      )}
    </>
  )
}
