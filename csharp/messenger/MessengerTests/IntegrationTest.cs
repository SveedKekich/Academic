namespace MessengerTests;

using MessengerApi.Data;
using System.Net.Http.Json;
using Microsoft.AspNetCore.Mvc.Testing;
using Microsoft.Extensions.DependencyInjection; 
using Xunit;

public class IntegrationTests : IClassFixture<WebApplicationFactory<Program>>
{
    private readonly HttpClient _client;

    public IntegrationTests(WebApplicationFactory<Program> factory)
    {
        _client = factory.CreateClient();

        using (var scope = factory.Services.CreateScope())
        {
            var db = scope.ServiceProvider.GetRequiredService<AppDbContext>(); 
            
            db.Database.EnsureCreated(); 
        }
        // ------------------------------------------------
    }

    public class UserResponse
    {
        public Guid Id { get; set; }
        public string Username { get; set; } = "";
    }
    


    [Fact]
    public async Task FullMessageFlow()
    {

var userAResponse = await _client.PostAsJsonAsync("/users", new { username = "Alice" });

if (!userAResponse.IsSuccessStatusCode)
{
    var errorBody = await userAResponse.Content.ReadAsStringAsync();
    throw new Exception($"API crashed with 500. Backend Exception Details:\n{errorBody}");
}

var userA = await userAResponse.Content.ReadFromJsonAsync<UserResponse>();

        var userBResponse = await _client.PostAsJsonAsync("/users",
            new { username = "Bob" });


        var userB = await userBResponse.Content
            .ReadFromJsonAsync<UserResponse>();


        if (userA == null || userB == null)
{
    throw new Exception("User creation failed - API returned null");
}
        var sendResponse = await _client.PostAsJsonAsync("/messages", new
        {
            senderId = userA!.Id,
            receiverId = userB!.Id,
            text = "Hello"
        });

        sendResponse.EnsureSuccessStatusCode();

        var response = await _client.GetAsync(
            $"/messages/{userA.Id}/{userB.Id}"
        );

        response.EnsureSuccessStatusCode();

        var history = await response.Content.ReadAsStringAsync();

        Assert.Contains("Hello", history);
    }
}