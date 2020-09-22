from mvc.models.repositories.note_repository import NoteRepository

class MainController(NoteRepository):
    def __init__(self):
        # Create note repository here
        # Your code here
        super().__init__()
        pass
    
    def get_all_notes(self):
        # Return all notes
        # Your code here
        return NoteRepository.get_all_notes(self)
        pass

    def add_note(self, note: str):
        # Add note
        # Your code here
        NoteRepository.add_note(self, note)
        pass

    def clear_all(self):
        # Clear all note
        # Your code here
        NoteRepository.clear_all_notes(self)
        pass
