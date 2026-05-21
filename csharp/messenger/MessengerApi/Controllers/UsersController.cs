using MessengerApi.Data;
using MessengerApi.DTOs;
using MessengerApi.Models;
using Microsoft.AspNetCore.Mvc;

namespace MessengerApi.Controllers;

[ApiController]
[Route("users")]
public class UsersController : ControllerBase
{
    private readonly AppDbContext _context;

    public UsersController(AppDbContext context)
    {
        _context = context;
    }

    [HttpPost]
    public async Task<IActionResult> Create(CreateUserDto dto)
    {
        if (string.IsNullOrWhiteSpace(dto.Username))
            return BadRequest("Username required");

        var user = new User
        {
            Username = dto.Username
        };

        _context.Users.Add(user);

        await _context.SaveChangesAsync();

        return Ok(user);
    }
}