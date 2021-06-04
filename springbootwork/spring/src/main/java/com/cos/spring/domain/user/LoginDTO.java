package com.cos.spring.domain.user;


import lombok.Data;

//DTO = Data Transfer Object
@Data
public class LoginDTO {
	private String username;
	private String password;
}
