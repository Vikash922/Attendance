import re

def fix():
    with open('app/src/main/java/com/example/presentation/screens/CashBookScreen.kt', 'r') as f:
        content = f.read()

    # Find the forEachIndexed start
    find_str = """                                HorizontalDivider(color = Color(0xFFE5E7EB), thickness = 1.dp)

                                // Table Items with Vertical Grid Dividers (Excel look)
                                displayTransactions.forEachIndexed { index, tx ->
                                    Row(
                                        modifier = Modifier
                                            .fillMaxWidth()
                                            .clickable { viewModel.openTransactionDetail(tx) }"""
    
    replace_str = """                                HorizontalDivider(color = Color(0xFFE5E7EB), thickness = 1.dp)
                        }
                    }
                    
                    itemsIndexed(
                        items = displayTransactions,
                        key = { _, tx -> tx.id }
                    ) { index, tx ->
                        Row(
                            modifier = Modifier
                                .fillMaxWidth()
                                .padding(horizontal = 12.dp)
                                .clickable { viewModel.openTransactionDetail(tx) }"""
                                
    # Find the end of the forEachIndexed block
    end_search = """                                    if (index < displayTransactions.size - 1) {
                                        HorizontalDivider(color = Color(0xFFE5E7EB), thickness = 1.dp)
                                    }
                                }
                            }
                        }
                    }
                }

                item { Spacer(modifier = Modifier.height(10.dp)) }"""
                
    end_replace = """                                    if (index < displayTransactions.size - 1) {
                                        HorizontalDivider(color = Color(0xFFE5E7EB), thickness = 1.dp)
                                    }
                                }

                } // Close itemsIndexed

                item { Spacer(modifier = Modifier.height(10.dp)) }"""
                
    
    if find_str in content:
        content = content.replace(find_str, replace_str)
        # Regex to find the end block because the spacer might be 16.dp instead of 10.dp
        
        # We need to remove 3 closing braces that correspond to the Column and item that we closed early.
        # Let's do it with regex.
        pattern = r"                                    if \(index < displayTransactions\.size - 1\) \{\n                                        HorizontalDivider\(color = Color\(0xFFE5E7EB\), thickness = 1\.dp\)\n                                    \}\n                                \}\n                            \}\n                        \}\n                    \}\n                \}\n\n                item \{ Spacer\(modifier = Modifier\.height\((\d+)\.dp\)\) \}"
        
        replacement = r"                                    if (index < displayTransactions.size - 1) {\n                                        HorizontalDivider(color = Color(0xFFE5E7EB), thickness = 1.dp)\n                                    }\n                                }\n\n                item { Spacer(modifier = Modifier.height(\1.dp)) }"
        
        content = re.sub(pattern, replacement, content)
        
        with open('app/src/main/java/com/example/presentation/screens/CashBookScreen.kt', 'w') as f:
            f.write(content)
        print("Fixed CashBookScreen.kt correctly")
    else:
        print("Could not find string in CashBookScreen.kt")

fix()
