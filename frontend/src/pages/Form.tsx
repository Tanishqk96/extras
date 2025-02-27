import { useState } from "react";
import axios from "axios";
interface FormData {
  name: string;
  email: string;
}

const Form = () => {
  const [formData, setFormData] = useState<FormData>({ name: "", email: "" });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
   
  try {
    const response = await axios.post(
      "http://127.0.0.1:5000/",
      {
        name: formData.name,
        email: formData.email,
      },
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    

    console.log("Response from backend:", response.data);
  } catch (error) {
    console.error("Error sending data:", error);
  }
  };


  return (
    <div className="flex items-center justify-center h-screen bg-gray-100">
      <form
        onSubmit={handleSubmit}
        className="bg-white p-6 rounded-lg shadow-md w-96"
      >
        <h2 className="text-2xl font-bold text-gray-700 text-center mb-4">
          Contact Form
        </h2>

        {/* Name Input */}
        <div className="mb-4">
          <label className="block text-gray-600 font-medium mb-1">Name</label>
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            className="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
            placeholder="Enter your name"
            required
          />
        </div>

        {/* Email Input */}
        <div className="mb-4">
          <label className="block text-gray-600 font-medium mb-1">Email</label>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            className="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
            placeholder="Enter your email"
            required
          />
        </div>

        {/* Submit Button */}
        <button
          type="submit"
          className="w-full bg-blue-500 text-white font-semibold py-2 rounded-md hover:bg-blue-600 transition duration-300"
        >
          Submit
        </button>
      </form>
    </div>
  );
};

export default Form;
