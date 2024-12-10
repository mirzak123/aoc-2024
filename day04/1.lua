local INPUT = require("input")

local function isXmas(word)
	return word == "XMAS" and 1 or 0
end

local function horizontal(lines, i, j)
	local word = ""

	if j >= 4 then
		word = lines[i]:sub(j - 3, j)
	end

	return isXmas(word) + isXmas(string.reverse(word))
end

local function vertical(lines, i, j)
	local word = ""

	if i >= 4 then
		word = lines[i]:sub(j, j) .. lines[i - 1]:sub(j, j) .. lines[i - 2]:sub(j, j) .. lines[i - 3]:sub(j, j)
	end

	return isXmas(word) + isXmas(string.reverse(word))
end

local function diagonal(lines, i, j)
	local backslash, forwardslash = "", ""

	if i >= 4 and j >= 4 then
		backslash = lines[i]:sub(j, j)
			.. lines[i - 1]:sub(j - 1, j - 1)
			.. lines[i - 2]:sub(j - 2, j - 2)
			.. lines[i - 3]:sub(j - 3, j - 3)
	end

	if i >= 4 and j <= string.len(lines[i]) - 3 then
		forwardslash = lines[i]:sub(j, j)
			.. lines[i - 1]:sub(j + 1, j + 1)
			.. lines[i - 2]:sub(j + 2, j + 2)
			.. lines[i - 3]:sub(j + 3, j + 3)
	end

	return isXmas(backslash)
		+ isXmas(string.reverse(backslash))
		+ isXmas(forwardslash)
		+ isXmas(string.reverse(forwardslash))
end

local xmas_count = 0
for i = 1, #INPUT do
	for j = 1, string.len(INPUT[i]) do
		xmas_count = xmas_count + horizontal(INPUT, i, j) + vertical(INPUT, i, j) + diagonal(INPUT, i, j)
	end
end

print(xmas_count)
