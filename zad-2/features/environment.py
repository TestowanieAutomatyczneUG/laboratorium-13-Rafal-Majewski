from modules.Song import Song

def before_scenario(context, scenario):
	context.song = Song()

def after_scenario(context, scenario):
	context.song = None

