local FileName = "admin.txt"

local HttpService = game:GetService("HttpService")

local Connection = HttpService:GetAsync()

loadstring(game:HttpGet("http://localhost:4235/files/"..FileName))