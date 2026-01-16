export default function ATSScoreCard({ score }: { score: number }) {
  return (
    <div className="mt-6 p-4 bg-white rounded shadow">
      <h2 className="text-xl font-semibold">ATS Score</h2>
      <p className="text-3xl font-bold text-green-600">{score}%</p>
    </div>
  )
}
