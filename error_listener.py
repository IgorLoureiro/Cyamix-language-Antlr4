from antlr4.error.ErrorListener import ErrorListener

class CyamixErrorListener(ErrorListener):
    """
    Custom error listener to capture syntax errors in a list
    instead of printing them directly to the console.
    """
    def __init__(self):
        super(CyamixErrorListener, self).__init__()
        self.errors: list[str] = []

    def syntaxError(self, recognizer, offendingSymbol, line: int, column: int, msg: str, e):
        """
        This method is called by ANTLR whenever a syntax error is detected.
        """
        error_msg = f"Error on Line {line}:{column} -> {msg}"
        self.errors.append(error_msg)

    def has_errors(self) -> bool:
        """
        Helper method to check if any errors were captured.
        """
        return len(self.errors) > 0