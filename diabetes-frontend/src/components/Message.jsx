export default function Message({ role, text }) {
  const isUser = role === "user";

  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
      <div
        className={`max-w-xl p-3 rounded-lg ${
          isUser ? "bg-green-600" : "bg-gray-700"
        }`}
      >
        {text}
      </div>
    </div>
  );
}