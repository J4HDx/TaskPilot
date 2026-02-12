import axios from 'axios';

// Use the environment variable for the API URL, with a fallback for local development.
const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

/**
 * Fetches all flows from the backend.
 */
export const getFlows = () => {
  return apiClient.get('/flows');
};

/**
 * Creates a new flow.
 * @param {object} flowData - The data for the new flow.
 */
export const createFlow = (flowData) => {
  return apiClient.post('/flows', flowData);
};

/**
 * Deletes a flow by its ID.
 * @param {string} flowId - The ID of the flow to delete.
 */
export const deleteFlow = (flowId) => {
  return apiClient.delete(`/flows/${flowId}`);
};

// You can add other API calls here as the application grows.
// For example:
//
// export const updateFlow = (flowId, flowData) => {
//   return apiClient.put(`/flows/${flowId}`, flowData);
// };
//
// export const getFlowById = (flowId) => {
//   return apiClient.get(`/flows/${flowId}`);
// };