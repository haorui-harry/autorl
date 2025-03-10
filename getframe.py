 
 
 def _save_frame(self, episode, step):
        """保存当前帧为图像文件"""
        frame = self._get_frame()
        if frame is None:
            return None
            
        plt.imshow(frame)
        plt.axis('off')
        filename = f"ep_{episode}_step_{step}.png"
        plt.savefig(filename, bbox_inches='tight')
        plt.close()
        
        # 转换为base64编码
        with open(filename, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode()
        
        return encoded_image