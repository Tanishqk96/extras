const { spawn } = require("child_process");

// Run the Python script
const pythonProcess = spawn("python3", ["script.py", "Node.js", "to", "Python"]);

// Capture stdout (output from Python script)
pythonProcess.stdout.on("data", (data) => {
    console.log(`Python Output: ${data.toString()}`);
});

// Capture stderr (errors from Python script)
pythonProcess.stderr.on("data", (data) => {
    console.error(`Python Error: ${data.toString()}`);
});

// Detect when the Python script has exited
pythonProcess.on("close", (code) => {
    console.log(`Python process exited with code ${code}`);
});
