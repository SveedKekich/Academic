using Microsoft.EntityFrameworkCore;
using MessengerApi.Models;

namespace MessengerApi.Data;

public class AppDbContext : DbContext
{
    public AppDbContext(DbContextOptions<AppDbContext> options)
        : base(options)
    {
    }

    public DbSet<User> Users => Set<User>();

    public DbSet<Message> Messages => Set<Message>();
}