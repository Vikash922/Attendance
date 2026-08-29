import re

def fix():
    with open('app/src/main/java/com/example/presentation/screens/CashBookScreen.kt', 'r') as f:
        content = f.read()

    # The goal is to replace `displayTransactions.forEachIndexed { index, tx ->` with `itemsIndexed(...)`
    # However, it is inside an `item { Column { ... } }` block.
    # We need to close the `item { Column {` block right before the forEach, and then start `itemsIndexed`.
    
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
                                
    # Also we need to remove the closing braces for `item { Column {` at the end of the `else` block.
    # The end of the transaction rendering looks like:
    #                                     )
    #                                 }
    #                                 HorizontalDivider(color = Color(0xFFF1F5F9), thickness = 1.dp)
    #                             }
    #                         }
    #                     }
    #                 }
    #             }
    
    if find_str in content:
        content = content.replace(find_str, replace_str)
        # Now remove two closing braces that belonged to `Column` and `item`
        # Because we closed them early.
        # We will search for the end of the items loop
        
        end_search = """                                    }
                                }

                                HorizontalDivider(color = Color(0xFFF1F5F9), thickness = 1.dp)
                            }
                        }
                    }
                }

                item { Spacer(modifier = Modifier.height(10.dp)) }"""
                
        end_replace = """                                    }
                                }

                                HorizontalDivider(color = Color(0xFFF1F5F9), thickness = 1.dp)
                            }
                }

                item { Spacer(modifier = Modifier.height(10.dp)) }"""
        
        content = content.replace(end_search, end_replace)
        with open('app/src/main/java/com/example/presentation/screens/CashBookScreen.kt', 'w') as f:
            f.write(content)
        print("Fixed CashBookScreen.kt")
    else:
        print("Could not find string in CashBookScreen.kt")

fix()
