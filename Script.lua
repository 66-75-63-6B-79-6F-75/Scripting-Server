--// this file is meant to be ran using a roblox executor

URL = "localhost" --// Or "https://abcdefg-abcdefg-abcdefg.ngrok.io"
FileName = "admin.txt"






local content
if URL == "localhost" then
    content = syn.request(
        {
            Url = "http://127.0.0.1:4235/files/"..FileName,  
            Method = "GET",
            Headers = {
                ["Content-Type"] = "application/json";
            },  
        }
    )
else
    content = syn.request(
        {
            Url = URL.."/files/"..FileName,  
            Method = "GET",
            Headers = {
                ["Content-Type"] = "application/json";
                ["Fix-Ngrok-Block"] = "ngrok-skip-browser-warning"
            },  
        }
    )
end

loadstring(content.Body)()