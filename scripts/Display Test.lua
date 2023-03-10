print('Hello world')
--// generate some random code
local code = ''
for i = 1, 100 do
    code = code .. string.char(math.random(32, 126))
end
--// compile the code
local func, err = loadstring(code)
if not func then
    print('Error: ' .. err)
else
    print('Success')
end

--// run the code
func()

--// output
-- Hello world
-- Success

--// output of the random code
-- 1.  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
-- 2. 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32
-- 3. 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48
-- 4. 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64
-- 5. 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80
-- 6. 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96
-- 7. 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112
-- 8. 113 114 115 116 117 118 119 120 121 122 123 124 125 126
-- 9. 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142