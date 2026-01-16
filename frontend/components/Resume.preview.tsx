export default function ResumePreview({ pdfUrl }: { pdfUrl: string }) {
  return (
    <div className="mt-6 bg-white p-4 rounded shadow">
      <h2 className="text-xl font-semibold mb-2">Resume Preview</h2>
      <iframe
        src={pdfUrl}
        className="w-full h-96 border"
      />
    </div>
  )
}
