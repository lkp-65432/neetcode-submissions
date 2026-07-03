class Solution:

    def encode(self, strs: List[str]) -> str:
        """编码：每个字符串前加长度+分隔符"""
        result = []
        for s in strs:
            result.append(str(len(s)) + "#" + s)
        return "".join(result)
    
    def decode(self, s: str) -> List[str]:
        """解码：按长度读取"""
        result = []
        i = 0
        while i < len(s):
            # 找到 # 的位置
            j = s.find("#", i)
            # 获取字符串长度
            length = int(s[i:j])
            # 提取字符串
            result.append(s[j+1:j+1+length])
            # 移动到下一个位置
            i = j + 1 + length
        return result
