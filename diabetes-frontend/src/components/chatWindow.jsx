import Message from "./Message";

export default function ChatWindow() {
  return (
    <div className="flex-1 flex flex-col">
      
      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        <Message role="user" text="What is diabetes?" />
        <Message role="bot" text="Diabetes is a condition where blood sugar levels are higher than normal." />
      </div>

      {/* Input */}
      <div className="border-t border-gray-700 p-4">
        <input
          className="w-full p-3 rounded bg-gray-800 outline-none"
          placeholder="Ask about diabetes..."
        />
      </div>

    </div>
  );
}
