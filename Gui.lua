--// Not finished

-- Create the GUI and its components
local gui = script.Parent
local scrollingFrame = gui:WaitForChild("ScrollingFrame")

-- Set the gap between buttons and the size of the buttons
local gap = 20
local buttonSize = UDim2.new(1, 0, 0, 50)

local folderUrl = "http://localhost:5000/files/" -- Replace this with the actual URL of the folder on your Flask server
local response = game:GetService("HttpService"):GetAsync(folderUrl)
local files = game:GetService("HttpService"):JSONDecode(response)

for _, file in pairs(files) do

	local button = Instance.new("TextButton")
	button.Name = "Button"
	button.Text = file.Name -- Set the button text to the name of the file
	button.Size = buttonSize


	local numButtons = #scrollingFrame:GetChildren()
	local buttonPosition = UDim2.new(0, 0, 0, (buttonSize.Y.Offset + gap) * numButtons)

	button.Position = buttonPosition

	button.Parent = scrollingFrame

	scrollingFrame.CanvasSize = scrollingFrame.CanvasSize + UDim2.new(0, 0, 0, buttonSize.Y.Offset + gap)

	button.MouseButton1Click:Connect(function()
		local fileUrl = folderUrl .. file.Name
		loadstring(game:HttpGet(fileUrl))()
	end)
end
