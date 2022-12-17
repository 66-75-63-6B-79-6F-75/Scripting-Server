--// this file is meant to be ran using a roblox executor

local FileName = "admin.txt"

local loads = loadstring(game:HttpGet("http://127.0.0.1:4235/files/"..FileName))
loads()