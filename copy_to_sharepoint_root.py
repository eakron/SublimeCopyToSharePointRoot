import sublime, sublime_plugin, subprocess, shutil

hive_location = "C:\\Program Files\\Common Files\\microsoft shared\\Web Server Extensions\\15\\TEMPLATE\\LAYOUTS\\"
separator = "Layouts\\"

class CopyToSharepointRootCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		src_path = self.view.file_name()

		if not separator in src_path:
			message = 'This script is only able to copy things to Layouts in hive.'
		else:
			dest_path = hive_location + src_path.split(separator)[-1]
			shutil.copyfile(src_path, dest_path)
			message = 'File uploaded to the hive.'

		sublime.status_message(message)
