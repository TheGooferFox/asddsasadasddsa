import json

alias = {
	  "bugz":       	"http://i.imgur.com/dWMFR68.jpg"
	, "paste":      	"Paste your code at http://p.ahkscript.org/"
	, "hello":      	"Hello {0.author.mention}!"
	, "mae":        	"*{0.author.mention} bows*"
	, "code":      		"To paste code type: `!hl [paste code here]`"
	, "shrug":			"¯\_(ツ)_/¯"
  	, "tutorial":       {"title": "Tutorial by tidbit", "description": "https://autohotkey.com/docs/Tutorial.htm"}
	, "documentation":  {"title": "AutoHotkey documentation", "description": "https://autohotkey.com/docs/AutoHotkey.htm"}
	, "forum":          {"title": "AutoHotkey forums", "description": "https://autohotkey.com/boards/"}
}

alias_assoc = {
	  "c": "code"
	, "p": "paste"
	, "tut": "tutorial"
	, "forums": "forum"
	, "ahk": "update"
	, "version": "update"
	, "hl": "highlight"
}

ignore_chan = [
	  'music'
	, 'irc'
	, 'reddit'
]

ignore_cmd = [
	  'clear'
	, 'mute'
	, 'levels'
	, 'rank'
	, 'mute'
	, 'unmute'
	, 'manga'
	, 'pokemon'
	, 'urban'
	, 'imgur'
	, 'anime'
	, 'twitch'
	, 'youtube'
]

del_cmd = [
	  'highlight'
	, 'mae'
]

ahk_char = 1920
ahk_line = 28

forum_char = 250
forum_line = 8

file = open("Docs.json", "r")
docs_assoc = json.loads(file.read())
file.close()
docs = []
for x in docs_assoc:
	docs.append(x)