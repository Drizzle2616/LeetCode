class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split the path by '/'
        components = path.split('/')
        stack = []
        
        for component in components:
            if component == '' or component == '.':
                # Ignore empty components and current directory
                continue
            elif component == '..':
                # Move up one directory level if possible
                if stack:
                    stack.pop()
            else:
                # Push the component to the stack
                stack.append(component)
        
        # Join the components in the stack to form the canonical path
        canonical_path = '/' + '/'.join(stack)
        return canonical_path
