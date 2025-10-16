import React, { useState, useEffect, useCallback } from 'react';
import FlowList from './components/FlowList';
import FlowForm from './components/FlowForm';
import * as api from './api/taskpilot';

function App() {
  const [flows, setFlows] = useState([]);
  const [error, setError] = useState(null);

  const fetchFlows = useCallback(async () => {
    try {
      const response = await api.getFlows();
      setFlows(response.data);
      setError(null);
    } catch (error) {
      console.error("Error fetching flows:", error);
      setError("Could not fetch flows. Is the backend running?");
    }
  }, []);

  useEffect(() => {
    fetchFlows();
  }, [fetchFlows]);

  const handleCreateFlow = async (flowData) => {
    try {
      await api.createFlow(flowData);
      fetchFlows(); // Refresh the list
    } catch (error) {
      console.error("Error creating flow:", error);
      setError("Failed to create flow.");
    }
  };

  const handleDeleteFlow = async (flowId) => {
    try {
      await api.deleteFlow(flowId);
      fetchFlows(); // Refresh the list
    } catch (error) {
      console.error("Error deleting flow:", error);
      setError("Failed to delete flow.");
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 text-gray-800">
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto py-4 px-4 sm:px-6 lg:px-8 flex items-center justify-between">
          <h1 className="text-2xl font-bold text-gray-900">
            TaskPilot Dashboard
          </h1>
        </div>
      </header>
      <main>
        <div className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
          {error && (
            <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative mb-4" role="alert">
              <strong className="font-bold">Error: </strong>
              <span className="block sm:inline">{error}</span>
            </div>
          )}
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
            <div className="lg:col-span-2">
              <h2 className="text-xl font-semibold mb-4">My Flows</h2>
              <FlowList flows={flows} onDelete={handleDeleteFlow} />
            </div>
            <div>
              <FlowForm onFlowCreate={handleCreateFlow} />
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;