APP_PACKAGE = "com.simplemobiletools.notes.pro"

class selectors:
    class material_toolbar: 
        search_tool = f'{APP_PACKAGE}:id/open_search'
        add_note = f'{APP_PACKAGE}:id/new_note'
        more_options = 'new UiSelector().description("More options")'
        
    class search_tool:
        search_field = f'{APP_PACKAGE}:id/search_query'
        search_previous = f'{APP_PACKAGE}:id/search_previous'
        search_next = f'{APP_PACKAGE}:id/search_next'
        search_clear = f'{APP_PACKAGE}:id//search_clear'
        
    class add_note:
        label_field = f'{APP_PACKAGE}:id/new_note_type_label'
        type_note_text = f'{APP_PACKAGE}:id/type_text_note'
        type_note_checklist = f'{APP_PACKAGE}:id/type_checklist'
        btn_ok = f'{APP_PACKAGE}:id/button1'
        btn_cancel = f'{APP_PACKAGE}:id/button2'
        toast_error = '//android.widget.Toast[@text="Please name your note"]'
        
    class more_options:
        share = f'new UiSelector().text("Share")'
        create_shortcut = 'new UiSelector().text("Create shortcut")'
        lock_note = 'new UiSelector().text("Lock note")'
        open_file = 'new UiSelector().text("Open file")'
        export_file = 'new UiSelector().text("Export as file")'
        print = 'new UiSelector().text("Print")'
        settings = 'new UiSelector().text("Settings")'
        about = 'new UiSelector().text("About")'
        
    class edit_text:
        add_text = 'com.simplemobiletools.notes.pro:id/text_note_view'