# src/database/models.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Table, Text, Enum as SQLEnum, PrimaryKeyConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import func
from src.databases.pg_manager import Base
import enum


# skill_user_association = Table(
#     'skill_user_association',
#     Base.metadata,
#     Column('user_id', Integer, ForeignKey('users.id', ondelete="CASCADE")),
#     Column('skill_id', Integer, ForeignKey('skills.id', ondelete="CASCADE")),
#     PrimaryKeyConstraint('user_id', 'skill_id')
# )


class SkillLevel(enum.Enum):
    beginner = "beginner"
    intermediate = "intermediate"
    advanced = "advanced"
    expert = "expert"
    

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    full_name = Column(String(100))
    bio = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_active = Column(Boolean, default=True)

    skills: Mapped[list["Skill"]] = relationship("Skill", secondary="users_skills", back_populates="users")


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False, index=True, unique=True)
    description = Column(Text, nullable=False)
    level = Column(SQLEnum(SkillLevel), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    users: Mapped[list["User"]] = relationship("User", secondary="users_skills", back_populates="skills")


class SkillUser(Base):
    __tablename__ = 'users_skills'

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    skill_id: Mapped[int] = mapped_column(Integer, ForeignKey("skills.id"))

    __table_args__ = (
        PrimaryKeyConstraint('user_id', 'skill_id', name="composite_key_users_skills"),
    )
