export default function Sidebar() {
  return (
    <div className="w-64 bg-gray-800 border-r border-gray-700 flex flex-col">
      
      <button className="m-4 p-2 rounded bg-green-600 hover:bg-green-700">
        + New Chat
      </button>

      <div className="flex-1 overflow-y-auto px-2 space-y-2">
        <div className="p-2 rounded bg-gray-700 cursor-pointer">
          Diabetes basics
        </div>
        <div className="p-2 rounded bg-gray-700 cursor-pointer">
          Diet questions
        </div>
      </div>

    </div>
  );
}
