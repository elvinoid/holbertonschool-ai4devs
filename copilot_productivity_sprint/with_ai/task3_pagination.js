function paginate(users, page = 1, limit = 10) {
  const start = (page - 1) * limit;
  const end = start + limit;

  return {
    page,
    limit,
    total: users.length,
    data: users.slice(start, end)
  };
}

module.exports = paginate;