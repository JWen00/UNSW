# 01 

## Understand your computer better

In languages like _C_, _C++_ and _Haskell_ a **compiler**  translates your code into a **target language** (e.g machine code) 

Alternatively, in languages like _Perl_, _Python_ and _Javascript_, an **interpreter executes a program from your code. 

Other languages use both! For example, _Java_ **compiles** and then **interprets** before getting to machine code. 

## Compilers 

Stages of a compiler 
1. Lexer 
    *  given an input, produces a stream of _tokens_ 
    
2. Parser 
    * converts the tokens in a **parse tree** or **abstract syntax tree**
    * structure of lexemes(tokens) to produce certain parse trees is **grammar**   

> NOTE: **Backus-Naur** have terminals & non terminals which specify grammatical structures 

3. Semantic Analyser 
    * Checks variable scoping 
    * Adds additional information to the parse tree 

4. Optimising (optional)(?) 
    * Loop unrolling, loop fusion, 
    * Inlining specialisation 
    * Can transform the tree dramatically 

5. Code Generator 
    * registers allocation and explicit control flow 
    * Links runtime systems 
    * Selects appropriate machine instructions 

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

Second half of week 1 lectures are in ipad. 