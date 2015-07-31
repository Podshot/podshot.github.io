# Example Filter that can be updated

# Will always need an update since the version number never changes
VERSION = "0.0.0"
UPDATE_URL = "http://podshot.github.io/update_json.json"

def perform(level, box, options):
    global editor
    try:
        editor
    except:
        import inspect
        editor = inspect.stack()[1][0].f_locals.get('self', None).editor
    editor.Notify("Running version: "+VERSION+" of this filter")