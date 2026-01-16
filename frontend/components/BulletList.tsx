export default function BulletList({ bullets }: { bullets: string[] }) {
  return (
    <div className="mt-6 bg-white p-4 rounded shadow">
      <h2 className="text-xl font-semibold mb-2">Resume Bullets</h2>
      <ul className="list-disc pl-6">
        {bullets.map((b, i) => (
          <li key={i}>{b}</li>
        ))}
      </ul>
    </div>
  )
}
