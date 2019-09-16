# 01 

Backus-Naur 
* terminals & non terminals 

## Stages of a compiler 
1. Program string => lexer 
2. Sequence of tokens => parser
3. Parse Tree => semantic analyser (findingt the mearning of a program) 
4. Annotated Parse Tree => optimiser 
*  Intermediate Represenation => Code Generator 
5. Machine Code

## Course Outline 
* Lexer (wk 1-3)
* Parsing (wk 1-3) 
* Semantics (focus) 

## Changing C code into Haskell 

```C
int foo() { 
    int i; 
    i = 11; 
    if (i > 5) { 
        i--; 
    }
    return i;
}
```

```hs
module Lexar where
import Data.lexer(...)
data Token = Ident String
            | LParen
            | LBrace
            | RBrace 
            | Semi 
            | Gt
            | Minus
            | Equals
            | Return 
            | Keyword Kwd 
            | Unknown 
            deriving Show

data Kwd = If | Return

recogniseKeyword :: String -> Token 
recogniseKetword "if" = Keyword If
recogniseKetword "return" = Keyword Return
recogniseKetword str = Ident Str

data MyList a = EmptyList | Node a (MyList a))
-- MyList a == [a] 
-- EmptyList == [] 
-- Node x xs == x : xs

-- Recurse through to find all the tokens
lexer :: String -> [Token]
lexer []       = [] 
lexer (' ':cs) = lexer cs
lexer (c:cs) isSpace = lexer cs
lexer ('(':cs) = lexer LParen
lexer (')':cs) = lexer cs
lexer ('/':'/':cs) = 
    let rest = dropWhile(/= '\n')
    in lexer rest
-- etc.. other tokens '{', '}'

-- Now, numbers 
    -- We can think of functions as primities as well 
    -- notDigit :: Char -> Bool 
    -- notDigit = not . isDigit (Composition Function) 
lexer (c:cs) 
    | isDigit c = 
        let (digits, rest) = (break (not . isDigit)) (c:cs) 
        in Number (read digits) : lexer rest

    | isAlpha c = 
        let (alphanums, rest) = span isAlphaNum (c:cs) 
        in reconiseKeyword alphanums : lexer rest 

    -- otherwise == true
    | otherwise = error "Unrecognised Token!"
```

Typically in a compiler, you don't write lexer like this - we need better error messages

```hs
Type LineNumber = int
lexer :: Int -> String -> [(Token, LineNumber)] 

-- Return a tuble of the token and LineNumber e.g
lexer n (' ':cs) = lexer n cs

-- Handling the newline char 
lexer n ('\n':cs) = lexer (n+1) cs
```

