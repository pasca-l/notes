-- Functions
{-
Functions must obey the following rules:
1. Must accept an input.
2. Must give an output; type of outputs must match for every control statements.
3. From the same function with the same input, the output must be identical.
-}

-- Variables
{-
A single variable can only be assigned once. However, not in the case when using GHCi.
-}

printXPlus1 x =
    x + y
    where
        y = 1
