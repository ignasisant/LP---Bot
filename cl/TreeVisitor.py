if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
    from .SkylineVisitor import SkylineVisitor
else:
    from SkylineParser import SkylineParser
    from SkylineVisitor import SkylineVisitor

class TreeVisitor(SkylineVisitor):
    def __init__(self):
        self.nivell = 0

    def visitSkyline(self, ctx:SkylineParser.SkylineContext):
        if ctx.getChildCount() == 1:
            n = next(ctx.getChildren())
            print("  " * self.nivell +
                  '(' +n.getText() + ')')
            self.nivell -= 1

        elif ctx.getChildCount() == 2:
            print('  ' *  self.nivell + 'MINUS(-)')
            self.nivell += 1
            self.visit(ctx.skyline(0))
            self.nivell -= 1

        elif ctx.getChildCount() == 3:
            if ctx.MES():
                print('  ' *  self.nivell + 'MES(+)')
                self.nivell += 1
                self.visit(ctx.skyline(0))
                self.nivell += 1
                self.visit(ctx.skyline(1))
                self.nivell -= 1
            elif ctx.MUL():
                print('  ' *  self.nivell + 'MUL(*)')
                self.nivell += 1
                self.visit(ctx.skyline(0))
                self.nivell += 1
                self.visit(ctx.skyline(1))
                self.nivell -= 1
            elif ctx.MINUS():
                print('  ' *  self.nivell + 'MINUS(-)')
                self.nivell += 1
                self.visit(ctx.skyline(0))
                self.nivell += 1
                self.visit(ctx.skyline(1))
                self.nivell -= 1
            elif ctx.IGUAL():
                print('  ' *  self.nivell + 'IGUAL(:=)')
                self.nivell += 1
                n = next(ctx.getChildren())
                print("  " * self.nivell +
                SkylineParser.symbolicNames[n.getSymbol().type] +
                  '(' +n.getText() + ')')
                self.nivell += 1
                self.visit(ctx.skyline(0))
                self.nivell -= 1
        elif ctx.getChildCount() == 4:
            n = next(ctx.getChildren())
            print("  " * self.nivell + 'SKYLINE')
            self.nivell += 1
            self.visit(ctx.skyline(0))
            self.nivell += 1 
            self.visit(ctx.skyline(1))
            n = next(ctx.getChildren())
            self.nivell -= 1            
        
        elif ctx.getChildCount() >= 7:
            print("  " * self.nivell+'(' +
            ctx.getText() + ')')

            

    

    
