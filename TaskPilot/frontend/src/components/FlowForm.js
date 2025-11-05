import React, { useState } from 'react';

// In a real app, this would likely come from an API endpoint
const availableConnectors = {
  triggers: [
    { name: 'gmail', event: 'new_email', label: 'Gmail: New Email' }
  ],
  actions: [
    { name: 'telegram', action: 'send_message', label: 'Telegram: Send Message' }
  ]
};

const FlowForm = ({ onFlowCreate }) => {
  const [name, setName] = useState('');
  // For simplicity, we'll use the first available trigger/action as default
  const selectedTrigger = availableConnectors.triggers[0];
  const selectedAction = availableConnectors.actions[0];

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!name.trim()) {
      alert('Please enter a name for the flow.');
      return;
    }

    const newFlow = {
      name,
      description: `Flow to send a Telegram message for new Gmail emails.`,
      trigger: {
        connector: selectedTrigger.name,
        event: selectedTrigger.event,
        // For the MVP, the config is hardcoded. A future version would have UI fields for this.
        config: { subject_contains: "invoice" }
      },
      action: {
        connector: selectedAction.name,
        action: selectedAction.action,
        // This text template uses keys from the (mock) Gmail trigger data.
        config: { text: "New invoice received!\nFrom: {from}\nSubject: {subject}" }
      },
      enabled: true,
    };

    onFlowCreate(newFlow);
    setName(''); // Reset form after submission
  };

  return (
    <div className="bg-white shadow-md rounded-lg p-6">
      <h2 className="text-xl font-semibold mb-4">Create New Flow</h2>
      <form onSubmit={handleSubmit}>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="flowName">
            Flow Name
          </label>
          <input
            id="flowName"
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="e.g., 'Send Telegram for New Invoices'"
            className="shadow-sm appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-indigo-400"
          />
        </div>

        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="trigger">
            1. When this happens... (Trigger)
          </label>
          <select id="trigger" disabled className="bg-gray-100 shadow-sm border rounded w-full py-2 px-3 text-gray-700">
            {availableConnectors.triggers.map(t => <option key={t.name}>{t.label}</option>)}
          </select>
        </div>

        <div className="mb-6">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="action">
            2. ...then do this (Action)
          </label>
          <select id="action" disabled className="bg-gray-100 shadow-sm border rounded w-full py-2 px-3 text-gray-700">
            {availableConnectors.actions.map(a => <option key={a.name}>{a.label}</option>)}
          </select>
          <p className="text-xs text-gray-500 mt-2">Note: Trigger/Action selection and configuration is fixed for the MVP.</p>
        </div>

        <div className="flex items-center justify-end">
          <button
            type="submit"
            className="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline transition duration-150 ease-in-out"
          >
            Create Flow
          </button>
        </div>
      </form>
    </div>
  );
};

export default FlowForm;