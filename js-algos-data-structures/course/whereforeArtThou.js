function whatIsInName(collection, source) {
  const arr = [];

  const keys = Object.keys(source);

  return collection.filter((x) =>
    keys.every((key) => x[key] == source[key] && x.hasOwnProperty(key)),
  );
}
