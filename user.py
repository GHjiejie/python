from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Literal


class User(BaseModel):
    name: Optional[str] = Field(default="Default Name", min_length=1, max_length=50)
    age: Optional[int] = Field(default=0, ge=0, le=120)
    baseInfo: Dict[str, Optional[str]] = Field(default_factory=dict)

    def get_info(self) -> str:
        return f"Name: {self.name}, Age: {self.age} , Base Info: {self.baseInfo}"


# 创建对象实例
user = User(name="Jie", age=18, baseInfo={"hobby": "reading", "city": None})
print(user.get_info())


status: Literal["active", "inactive", "banned"] = "active"
arrray: List[float] = [1.0, 2.5, 3.3, 4.8]
print(f"User status: {status}")
print(f"Array values: {arrray}")
