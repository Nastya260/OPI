    def show_sessions(self):
        # Assuming sessions is a list of available sessions from the database
        sessions = self.database.read_sessions()

        if sessions:
            print("Available sessions:")
            for session in sessions:
                print(f"{session['id']}. {session['movie']} - {session['time']}")
