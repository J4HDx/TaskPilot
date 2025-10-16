import React from 'react';

const FlowList = ({ flows, onDelete }) => {
  if (flows.length === 0) {
    return (
      <div className="text-center p-8 bg-white rounded-lg shadow">
        <h3 className="text-lg font-medium text-gray-900">No Flows Yet</h3>
        <p className="mt-1 text-sm text-gray-500">Create a new flow on the right to get started!</p>
      </div>
    );
  }

  return (
    <div className="bg-white shadow overflow-hidden sm:rounded-lg">
      <ul className="divide-y divide-gray-200">
        {flows.map((flow) => (
          <li key={flow.id}>
            <div className="px-4 py-4 sm:px-6 hover:bg-gray-50">
              <div className="flex items-center justify-between">
                <p className="text-md font-medium text-indigo-600 truncate">{flow.name}</p>
                <div className="ml-2 flex-shrink-0 flex">
                  <span
                    className={`px-2 inline-flex text-xs leading-5 font-semibold rounded-full ${
                      flow.enabled ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'
                    }`}
                  >
                    {flow.enabled ? 'Enabled' : 'Disabled'}
                  </span>
                </div>
              </div>
              <div className="mt-2 sm:flex sm:justify-between">
                <div className="sm:flex">
                  <p className="flex items-center text-sm text-gray-600">
                    <span className="font-semibold mr-1">Trigger:</span> {flow.trigger.connector} ({flow.trigger.event})
                  </p>
                  <p className="mt-1 flex items-center text-sm text-gray-600 sm:mt-0 sm:ml-6">
                    <span className="font-semibold mr-1">Action:</span> {flow.action.connector} ({flow.action.action})
                  </p>
                </div>
                <div className="mt-4 flex-shrink-0 sm:mt-0 sm:ml-5">
                  <button
                    onClick={() => onDelete(flow.id)}
                    className="font-medium text-red-600 hover:text-red-500 transition duration-150 ease-in-out"
                  >
                    Delete
                  </button>
                </div>
              </div>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default FlowList;