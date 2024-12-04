local INPUT = require("input")

local function isMas(word)
	return word == "MAS"
end

local function diagonal(lines, i, j)
	local backslash, forwardslash = "", ""

	if i >= 2 and j >= 2 and i <= #lines - 1 and j <= string.len(lines[i]) - 1 then
		backslash = lines[i - 1]:sub(j - 1, j - 1) .. lines[i]:sub(j, j) .. lines[i + 1]:sub(j + 1, j + 1)
		forwardslash = lines[i + 1]:sub(j - 1, j - 1) .. lines[i]:sub(j, j) .. lines[i - 1]:sub(j + 1, j + 1)
	end

	return (
		(isMas(forwardslash) or isMas(string.reverse(forwardslash)))
		and (isMas(backslash) or isMas(string.reverse(backslash)))
	)
end

local xmas_count = 0
for i = 1, #INPUT do
	for j = 1, string.len(INPUT[i]) do
		if INPUT[i]:sub(j, j) == "A" and diagonal(INPUT, i, j) then
			xmas_count = xmas_count + 1
		end
	end
end

print(xmas_count)
