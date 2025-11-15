from grammar.CyamixVisitor import CyamixVisitor
from grammar.CyamixParser import CyamixParser
from antlr4.tree.Tree import TerminalNode
from antlr4 import ParserRuleContext

class SemanticAnalyzer(CyamixVisitor):
    def __init__(self):
        self.symbols = {}
        self.semantic_errors = []

    def report_error(self, line, col, message):
        """Helper function to format and store errors."""
        self.semantic_errors.append(f"Semantic Error on Line {line}:{col} -> {message}")

    def check_numeric_compatibility(self, op_type: str, left_type: str, right_type: str, ctx: ParserRuleContext) -> str:
        """
        Checks if types are compatible for arithmetic operations (+, *, /, -, etc.)
        Returns the resulting type ('int', 'float') or 'error_type'.
        """
        numeric_types = {'int', 'float', 'char'} 

        if op_type == '+':
            if 'string' in (left_type, right_type) and left_type != right_type:
                self.report_error(ctx.start.line, ctx.start.column,
                                 f"Invalid types for operator '{op_type}'. Cyamix does not support concatenation of '{left_type}' and '{right_type}'.")
                return 'error_type'
            elif left_type == 'string' and right_type == 'string':
                return 'string' 

        if left_type not in numeric_types or right_type not in numeric_types:
            if left_type != 'error_type' and right_type != 'error_type':
                self.report_error(ctx.start.line, ctx.start.column,
                                 f"Invalid types for operator '{op_type}'. Expected numeric types, got '{left_type}' and '{right_type}'.")
            return 'error_type'

        if 'float' in (left_type, right_type) or op_type in ('/', '÷'):
            return 'float'
        
        if 'char' in (left_type, right_type) or op_type in ('+', '-', '*'):
            return 'int'

        return 'int'

    def check_boolean_compatibility(self, op_type: str, left_type: str, right_type: str, ctx: ParserRuleContext) -> bool:
        """
        Checks if types are compatible for logical operations (&&, ||).
        Returns True if compatible (resulting type is 'boolean'), False otherwise.
        """
        if left_type != 'boolean' or right_type != 'boolean':
            if left_type != 'error_type' and right_type != 'error_type':
                self.report_error(ctx.start.line, ctx.start.column,
                                 f"Invalid types for logical operator '{op_type}'. Expected 'boolean', got '{left_type}' and '{right_type}'.")
            return False
        return True

    def visit(self, tree):
        """Standard visit method to skip TerminalNodes, which have no logic."""
        if tree is None or isinstance(tree, TerminalNode):
            return 
        return super().visit(tree)

    def visitChildren(self, node):
        """Default behavior for non-semantic rules: just continue visiting children."""
        if node.children:
            for child in node.children:
                self.visit(child)
        return
        
    def visitVarDecl(self, ctx: CyamixParser.VarDeclContext):
        """Handles variable declaration (type checking and symbol table entry)."""
        var_type = self.visit(ctx.type_())

        items = ctx.varItem()
        for item in items:
            var_name = item.ID().getText()

            if var_name in self.symbols:
                self.report_error(item.ID().symbol.line, item.ID().symbol.column, f"Variable '{var_name}' already declared.")
            else:
                self.symbols[var_name] = var_type

            if item.expr():
                expr_type = self.visit(item.expr()) 
                if expr_type != 'error_type' and expr_type != var_type:
                    self.report_error(ctx.start.line, ctx.start.column, f"Type mismatch: cannot assign '{expr_type}' to variable '{var_name}' of type '{var_type}'.")
            
    def visitAssignment(self, ctx: CyamixParser.AssignmentContext):
        """Handles simple assignment (x = expr;)."""
        var_name = ctx.ID().getText()
        
        if var_name not in self.symbols:
            self.report_error(ctx.ID().symbol.line, ctx.ID().symbol.column, f"Variable '{var_name}' not declared.")
            return
        
        target_type = self.symbols[var_name]
        expr_type = self.visit(ctx.expr())

        if expr_type != 'error_type' and target_type != expr_type:
            self.report_error(ctx.start.line, ctx.start.column, f"Type mismatch: cannot assign '{expr_type}' to variable '{var_name}' of type '{target_type}'.")
    
    def visitExpr(self, ctx: CyamixParser.ExprContext):
        return self.visit(ctx.logicalOrExpr())

    def visitLogicalOrExpr(self, ctx: CyamixParser.LogicalOrExprContext):
        type_left = self.visit(ctx.logicalAndExpr(0))
        
        for i in range(1, len(ctx.logicalAndExpr())):
            op_symbol = ctx.getChild(2 * i - 1).getText()
            type_right = self.visit(ctx.logicalAndExpr(i))
            
            if not self.check_boolean_compatibility(op_symbol, type_left, type_right, ctx):
                return 'error_type'
            type_left = 'boolean'
        return type_left

    def visitLogicalAndExpr(self, ctx: CyamixParser.LogicalAndExprContext):
        type_left = self.visit(ctx.equalityExpr(0))
        
        for i in range(1, len(ctx.equalityExpr())):
            op_symbol = ctx.getChild(2 * i - 1).getText()
            type_right = self.visit(ctx.equalityExpr(i))
            
            if not self.check_boolean_compatibility(op_symbol, type_left, type_right, ctx):
                return 'error_type'
            type_left = 'boolean'
        return type_left

    def visitEqualityExpr(self, ctx: CyamixParser.EqualityExprContext):
        if len(ctx.children) > 1:
            type_left = self.visit(ctx.relationalExpr(0))
            type_right = self.visit(ctx.relationalExpr(1))
            op_symbol = ctx.getChild(1).getText()
            
            if type_left != type_right and (type_left not in {'int', 'float', 'char'} or type_right not in {'int', 'float', 'char'}):
                 self.report_error(ctx.start.line, ctx.start.column, f"Invalid types for equality operator '{op_symbol}'. Cannot compare '{type_left}' with '{type_right}'.")
                 return 'error_type'

            return 'boolean'
        return self.visit(ctx.relationalExpr(0))

    def visitRelationalExpr(self, ctx: CyamixParser.RelationalExprContext):
        if len(ctx.children) > 1:
            type_left = self.visit(ctx.additiveExpr(0))
            type_right = self.visit(ctx.additiveExpr(1))
            op_symbol = ctx.getChild(1).getText()
            
            if self.check_numeric_compatibility(op_symbol, type_left, type_right, ctx) == 'error_type':
                return 'error_type'
            
            return 'boolean'
        return self.visit(ctx.additiveExpr(0))

    def visitAdditiveExpr(self, ctx: CyamixParser.AdditiveExprContext):
        type_left = self.visit(ctx.multiplicativeExpr(0))
        
        for i in range(1, len(ctx.multiplicativeExpr())):
            op_symbol = ctx.getChild(2 * i - 1).getText()
            type_right = self.visit(ctx.multiplicativeExpr(i))
            
            type_left = self.check_numeric_compatibility(op_symbol, type_left, type_right, ctx)
            if type_left == 'error_type':
                return 'error_type'
        return type_left

    def visitMultiplicativeExpr(self, ctx: CyamixParser.MultiplicativeExprContext):
        type_left = self.visit(ctx.unaryExpr(0))
        
        for i in range(1, len(ctx.unaryExpr())):
            op_symbol = ctx.getChild(2 * i - 1).getText()
            type_right = self.visit(ctx.unaryExpr(i))
            
            type_left = self.check_numeric_compatibility(op_symbol, type_left, type_right, ctx)
            if type_left == 'error_type':
                return 'error_type'
        return type_left

    def visitUnaryExpr(self, ctx: CyamixParser.UnaryExprContext):
        if ctx.primary():
            return self.visit(ctx.primary())
        
        op_symbol = ctx.getChild(0).getText()
        child_type = self.visit(ctx.unaryExpr())

        if op_symbol == '!':
            if child_type != 'boolean':
                self.report_error(ctx.start.line, ctx.start.column, f"Invalid type for unary operator '!'. Expected 'boolean', got '{child_type}'.")
                return 'error_type'
            return 'boolean'
        
        if child_type not in {'int', 'float', 'char'}:
             self.report_error(ctx.start.line, ctx.start.column, f"Invalid type for unary operator '{op_symbol}'. Expected numeric, got '{child_type}'.")
             return 'error_type'
        
        return child_type

    def visitPrimary(self, ctx: CyamixParser.PrimaryContext):
        """Returns the type of basic values (literals or variable IDs)."""
        if ctx.INT_LITERAL():
            return 'int'
        if ctx.FLOAT_LITERAL():
            return 'float'
        if ctx.CHAR_LITERAL():
            return 'char'
        if ctx.BOOL_LITERAL():
            return 'boolean'
        if ctx.STRING_LITERAL():
            return 'string'
        
        if ctx.ID():
            var_name = ctx.ID().getText()
            if var_name not in self.symbols:
                self.report_error(ctx.start.line, ctx.start.column, f"Variable '{var_name}' used before declaration.")
                return 'error_type'
            return self.symbols.get(var_name)
        
        if ctx.expr():
            return self.visit(ctx.expr())
            
        return 'unknown'
    
    def visitType(self, ctx: CyamixParser.TypeContext):
        """Returns the declared type name as a string."""
        return ctx.getText()