class Solution(object):
    @staticmethod
    def extract_depth_filename(line, max_depth):
        nspaces = 0
        depth = 0
        
        i = 0
        while depth < max_depth and i < len(line):
            if line[i] == '\t':
                depth += 1
            elif line[i] == ' ':
                nspaces += 1
                if nspaces == 4:
                    nspaces = 0
                    depth += 1
            else:
                break
                    
            i += 1
            
        return depth, line[i - nspaces:].rstrip()
    
    @staticmethod
    def is_file(path):
        return path.find('.') != -1
        
        
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        dir_stack = [] # stack of directory (lengths)
        max_path_length = 0
        
        for line in str.splitlines(input.encode('ascii')):
            depth, name = Solution.extract_depth_filename(line, len(dir_stack))
            while len(dir_stack) > depth:
                dir_stack.pop()
                
            cur_dir_length = dir_stack[-1] if dir_stack else 0
            
            if Solution.is_file(name):
                max_path_length = max(max_path_length, cur_dir_length + len(name))
            else:
                dir_stack.append(cur_dir_length + len(name)+1) # including '/'
                
        return max_path_length
